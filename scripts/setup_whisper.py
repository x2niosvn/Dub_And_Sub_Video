"""Cài đặt Whisper ASR vào virtualenv riêng (.venv-whisper).

Chạy 1 lần:
    py scripts/setup_whisper.py

Sau khi cài, faster-whisper + ctranslate2 chạy trong .venv-whisper
qua tiến trình con (asr_whisper_worker.py) — không cần bundle trong exe,
giảm ~112 MB kích thước bản phân phối.

Các bước đều resume-safe — chạy lại sẽ bỏ qua phần đã xong:

1. Tạo virtualenv .venv-whisper (Python hiện tại)
2. pip install faster-whisper<2.0
3. Tải model Whisper về models/whisper/
4. Smoke test: nhận dạng 1 file 2 giây → installed_ok.json
"""

import json
import os
import subprocess
import sys
import wave

sys.stdout.reconfigure(encoding="utf-8", errors="replace")


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

VENV_DIR = os.path.join(PROJECT_ROOT, ".venv")

VENV_PY = os.path.join(
    VENV_DIR,
    "Scripts" if os.name == "nt" else "bin",
    "python.exe" if os.name == "nt" else "python",
)

MODEL_DIR = os.path.join(
    PROJECT_ROOT,
    "models",
    "whisper",
)

MARKER = os.path.join(
    MODEL_DIR,
    "installed_ok.json",
)


# Chốt trần major.
# faster-whisper / ctranslate2 có thể thay đổi API giữa các major version.
_WHISPER_SPEC = "faster-whisper<2.0"


# Worker script của app.
WORKER = os.path.join(
    PROJECT_ROOT,
    "autodub",
    "speech",
    "asr_whisper_worker.py",
)

# Một số bản build có thể đặt worker trong data/_internal.
if not os.path.isfile(WORKER):
    for _d in ("data", "_internal"):
        _candidate = os.path.join(
            PROJECT_ROOT,
            _d,
            "autodub",
            "speech",
            "asr_whisper_worker.py",
        )

        if os.path.isfile(_candidate):
            WORKER = _candidate
            break


def log(msg: str) -> None:
    print(f"[setup-whisper] {msg}", flush=True)


def step_venv() -> None:
    """Tạo virtualenv nếu chưa tồn tại."""

    if os.path.isfile(VENV_PY):
        log("venv .venv-whisper đã có — bỏ qua")
        return

    log("tạo virtualenv .venv-whisper ...")

    subprocess.run(
        [
            sys.executable,
            "-m",
            "venv",
            VENV_DIR,
        ],
        check=True,
    )


def step_install() -> None:
    """Cài faster-whisper nếu chưa có."""

    probe = subprocess.run(
        [
            VENV_PY,
            "-c",
            "import faster_whisper",
        ],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )

    if probe.returncode == 0:
        log("faster-whisper đã cài — bỏ qua")
        return

    log("cài faster-whisper (ctranslate2, CPU/GPU) ...")

    subprocess.run(
        [
            VENV_PY,
            "-m",
            "pip",
            "install",
            "--quiet",
            _WHISPER_SPEC,
        ],
        check=True,
    )


def step_smoke() -> None:
    """Chạy smoke test Whisper worker."""

    if os.path.isfile(MARKER):
        log("smoke test đã đạt — bỏ qua")
        return

    if not os.path.isfile(WORKER):
        raise SystemExit(
            f"!! không thấy worker script: {WORKER}"
        )

    os.makedirs(MODEL_DIR, exist_ok=True)

    # Tạo WAV 2 giây im lặng, 16 kHz, mono, PCM 16-bit.
    smoke_wav = os.path.join(
        MODEL_DIR,
        "smoke_test.wav",
    )

    with wave.open(smoke_wav, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(16000)
        wf.writeframes(b"\x00\x00" * 32000)

    log(
        "chạy smoke test "
        "(tải model lần đầu có thể mất vài phút) ..."
    )

    try:
        proc = subprocess.run(
            [
                VENV_PY,
                WORKER,
                "--audio",
                smoke_wav,
                "--model",
                "medium",
                "--language",
                "zh",
                "--model-dir",
                MODEL_DIR,
            ],
            input='{"audio": ""}\n',
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=600,
        )

    finally:
        try:
            os.remove(smoke_wav)
        except OSError:
            pass

    stdout = proc.stdout or ""
    stderr = proc.stderr or ""

    lines = [
        line.strip()
        for line in stdout.splitlines()
        if line.strip()
    ]

    # Worker trả JSON theo từng dòng.
    ok = any(
        '"done"' in line
        for line in lines
    )

    if not ok:
        raise SystemExit(
            f"!! smoke test thất bại "
            f"(exit {proc.returncode}):\n"
            f"{stdout[-1000:]}\n"
            f"{stderr[-1000:]}"
        )

    with open(
        MARKER,
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(
            {
                "ok": True,
                "model": "medium",
                "backend": "faster-whisper",
            },
            f,
            ensure_ascii=False,
            indent=2,
        )

    log("smoke test PASS")


def main() -> None:
    log(
        "Cài đặt Whisper ASR vào venv riêng "
        "— giảm ~112 MB kích thước exe"
    )

    log(
        f"Model cache: {MODEL_DIR}"
    )

    step_venv()
    step_install()
    step_smoke()

    log(
        "XONG — Whisper chạy trong "
        ".venv-whisper (không bundle trong exe)."
    )


if __name__ == "__main__":
    main()