# ConsoleFileManager
This is a simple console file manager written on Python

~First things first:
1. Run <code>python manager.py create</code> to create catalog with files to test on. Catalog is found in C:\FileCatalog\
2. Use manager.py via console for test purposes.
3. To run unittests use console: <br>
<code>python manager_test.py</code> <br> 
<code>python utils/funcs_test.py</code>


Commands to use via command line:

-h --help - shows help message

<code>copy src dst</code> - copies file specified in <code>src</code> (fullpath) to file <code>dst</code> (fullpath).
You can omit <code>dst</code>, it will then copy with default name srcname_copy.

<code>delete src</code> - deletes <code>src</code> file or folder

<code>nf src</code> - counts number of files in <code>src</code> folder and it's subfolders

<code>search string</code> - searches files with <code>string</code> in filename and lists it

<code>add src</code> - recursevily adds creation date from metadata to file names in <code>src</code> folder

<code>analyse src</code> - recursevily analyses folders and subfolders in <code>src</code> for file size, lists total folder size in Mb
