# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

`which [app]` Shows which [app] will be run by default. 
`tail -f file` Outputs the contents of a file as it grows, starting with the last 10 lines.
`kill [pid]` Kills process with id [pid]
`grep [pattern] [files]` Search for [pattern] in [files]
`[command] | grep [pattern]` Searches for [pattern] in the output of [command]
`location [file]` Find all instances of [file]
`cat > [file]` Places standard input into [file]
`head [file]` Outputs the first 10 lines of [file]
`gzip [file]` Compresses [file] and renames it to [file].gz
`cat /proc/meminfo` Memory information

---

###Q2.  List Files in Unix   

What do the following commands do: 
`ls` List items in a directory
`ls -a` List items in a directory including dot files.
`ls -l` Displays the long format list of items in a directory.
`ls -lh` Displays the long format list of items in a directory. `h` does not exist as an option.
`ls -lah` Displays the long format list of items in a directory, including hidden files. `h` does not exist as an option.
`ls -t` Displays newest files first. (based on timestamp)
`ls -Glp` Displays the long format listing, but exclude the owner name. Directories include a `/`.

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

`-c` Displays files by file timestamp.
`-d` Displays only directories.
`-m` Displays the names as a comma-separated list.
`-r` Displays files in reverse order.
`-t` Displays newest files first. (based on timestamp)

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

xargs is a command on Unix and most Unix-like operating systems used to build and execute command lines from standard input. Commands such as grep and awk can accept the standard input as a parameter, or argument by using a pipe. However, others such as cp and echo disregard the standard input stream and rely solely on the arguments found after the command. 

`find /path -type f -print | xargs rm`

In the above example, the find utility feeds the input of xargs with a long list of file names. xargs then splits this list into sublists and calls rm once for every sublist.


 

