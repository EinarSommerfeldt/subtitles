# subtitles
Code for fixing subtitles. 

Can pad to make subtitles appear on screen longer, 

shift subtitles so they appear at the right time, 

shift progressively if subtitles get out of sync as time goes on.

Choose parameters in config. 

How to use progressive shifting:

1. Shift subtitles so they are synced correctly at some time.
2. Use new srt file as input.
3. Set progressive_shifting=1
4. Set shift=0.
5. Don't change padding from what you used when syncing.
6. Set time subtitles are synced as first_time in config.
8. Find another point later when they are out of sync again,
8. Set second_time = time the correct subtitles appear.
9. Set interval_shift as how long the subtitles were delayed.
