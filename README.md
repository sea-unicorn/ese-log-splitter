Are you too lazy to maintain your log file? Got 2 weeks of logs accumulated in the same file? Feeling sad that ESO Logs Uploader split feature does not actually work? Here is a solution for you. ESO Logs splitter tool that is capable to split any size of ESO Log file so long as you have space.

**Usage guide:**

1. Open it
2. Click "Browse" and find the ESO Encounter.log file
3. Click "Split"
4. Wait, it will notify you of the progress and what kind of raids it found so far.
5. Once finished - it will make a smaller log files if individual raids, such that resets of the team that has similar roster (6 ppl with same name at the moment) and went to the same trial - it will be in the same log file. 
6. Those individual log files will be placed in the "To upload" sub-directory at the same location where the ESO log splitter is located.
7. Do not forget to delete the original and split files after you done uploading them. If you happen to select invalid file - it will just copy it over to the "To upload" directory.
8. If you do not have enough disk space it will probably break as I do not have error handling for that.

**Notes:**

It will make a config file that helps is to remember selected ESO Log file from the previous operation. If you delete it - you will have to manually navigate to the log file next time you open it.
Script is made with Python 3.8
You do need a python compiler to compile the script into executable. Such as Pyinstaller.
