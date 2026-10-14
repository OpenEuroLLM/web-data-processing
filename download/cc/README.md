# CC downloading on LUMIO
0. Collect IDs of the crawls to download in `cc_list_latest.txt` (edit this file).
1. `get_url_lists.sh` downloads url lists for the crawls in `cc_list_latest.txt` 
2. `sbatch --partition small --cpus-per-task=32 --mem-per-cpu=1750M --time=72:00:00 -A project_465001890 download_crawl_rclone.sh warcpaths/CC-MAIN-2025-26.lst` runs the downloading job. 

NB! Change the project number above to the project you want to consume CPU-hours from. 
NB! The downloading job may finish before the whole crawl is downloaded due to time lumits in the `small` partition (3days). Restart it until you see "There was nothing to transfer" in the logs for the crawl.
