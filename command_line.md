### Terminal Commands Cheatsheet: [Terminal Commands Cheatsheet](https://github.com/0nn0/terminal-mac-cheatsheet)

### The following examples are for MacOS
#### 1. The steps of setting a variable in ternimal and make it work
 - **Open Terminal**: You can find it in the Applications folder or search for it using Spotlight (Command + Space).
 - **Edit Bash Profile**: Use the command **`nano ~/.bash_profile`** or **`nano ~/.zshrc`** (for newer MacOS versions) to open the profile file in a text editor.
 - **Add Environment Variable**: In the editor, add the line below, replacing **`your-api-key-here`** with your actual API key:
    **`export OPENAI_API_KEY='your-api-key-here'`**
 - **Save and Exit**: Press Ctrl+O to write the changes, followed by Ctrl+X to close the editor.
 - **Load Your Profile**: Use the command **`source ~/.bash_profile`** or **`source ~/.zshrc`** to load the updated profile.
 - **Verification**: Verify the setup by typing **`echo $OPENAI_API_KEY`** in the terminal. It should display your API key. echo acts like print, so it prints the **`OPENAI_API_KEY` variable**

#### 2. `**mv**` to move a file to a new directory or change its name.
    1. `mv [test.py](http://test.py) [test2.py](http://test2.py)` → change file name
    2. `mv [test.py](http://test.py) ../test` → move to a new folder called test
#### 3. `**rm**` delete files, `rm -r [folder]` you can use this to delete a folder
#### 4. `**which [program]**` tells you where your programm is in the folders listed in the PATH enviroment variable
#### 5. To show enviroment variable name, you can do like `echo $HOME` this means that show the variable name HOME’s string value
