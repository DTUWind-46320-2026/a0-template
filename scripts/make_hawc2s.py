"""Make HAWC2S files from a master htc file.

See A0 prompt for details.

Requires myteampack (which requires lacbox).
"""

from pathlib import Path

from a0pack import MyHTC

# file names and paths
SCRIPT_DIR = Path(__file__).parent
MASTER_FILE = (
    SCRIPT_DIR / ".." / "hawc_files" / "_master" / "dtu_10mw.htc"
)  # switch to your design when you have it!
SAVE_HAWC2S_DIR = SCRIPT_DIR / ".." / "hawc_files" / "htc_hawc2s"

# make rigid hawc2s file for single-wsp opt file
htc = MyHTC(MASTER_FILE)
htc.make_hawc2s(
    SAVE_HAWC2S_DIR,
    rigid=True,
    append="_hawc2s_1wsp",
    opt_path="./data/dtu_10mw_1wsp.opt",
    compute_steady_states=True,
    save_power=True,
)

# make rigid hawc2s file for multi-tsr opt file
htc = MyHTC(MASTER_FILE)
# INSERT CODE HERE WHEN PROMPTED (A0)
