"""Kiểm tra tiến trình chấm nhận bản vá NumPy, không cần dữ liệu lab."""

import subprocess
from pathlib import Path

from evaluate_practice import run_trackeval


def test_numpy_aliases_reach_evaluation_process(tmp_path: Path) -> None:
    """Script con dùng được tên NumPy cũ và nhận đúng tham số chấm."""
    scripts = tmp_path / "scripts"
    scripts.mkdir()
    (scripts / "run_mot_challenge.py").write_text(
        "import sys\nimport numpy as np\n"
        "assert np.float is float\nassert np.int is int\n"
        "assert sys.argv[sys.argv.index('--SEQ_INFO') + 1] == 'video_1'\n"
        "assert sys.argv[sys.argv.index('--BENCHMARK') + 1] == 'LAB21'\n",
        encoding="utf-8",
    )
    run_trackeval(tmp_path, "thu_nghiem", "LAB21", "train")


def test_evaluation_failure_is_reported(tmp_path: Path) -> None:
    """Lỗi của công cụ chấm được truyền về, không báo thành công giả."""
    import pytest

    scripts = tmp_path / "scripts"
    scripts.mkdir()
    (scripts / "run_mot_challenge.py").write_text("raise SystemExit(3)\n")
    with pytest.raises(subprocess.CalledProcessError):
        run_trackeval(tmp_path, "thu_nghiem", "LAB21", "train")
