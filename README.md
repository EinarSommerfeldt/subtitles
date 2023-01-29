# subtitles
Code for editing subtitles

Choose parameters in config. 

How to use progressive shifting:

1. Shift subtitles so they are synced correctly at some time.
2. Use new srt file as input.
3. Set shift=0.
4. Don't change padding from what you used when syncing.
5. Set time they are synced as first_time in config.
6. Find another point later when they are out of sync again,
7. Set second_time = time the correct subtitles appear.
8. Set interval_shift as how long the subtitles were delayed.
