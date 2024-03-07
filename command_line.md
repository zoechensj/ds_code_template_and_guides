The steps of setting a variable in ternimal and make it work

1. **Open Terminal**: You can find it in the Applications folder or search for it using Spotlight (Command + Space).
2. **Edit Bash Profile**: Use the command **`nano ~/.bash_profile`** or **`nano ~/.zshrc`** (for newer MacOS versions) to open the profile file in a text editor.
3. **Add Environment Variable**: In the editor, add the line below, replacing **`your-api-key-here`** with your actual API key:
    
    **`export OPENAI_API_KEY='your-api-key-here'`**
    
4. **Save and Exit**: Press Ctrl+O to write the changes, followed by Ctrl+X to close the editor.
5. **Load Your Profile**: Use the command **`source ~/.bash_profile`** or **`source ~/.zshrc`** to load the updated profile.
6. **Verification**: Verify the setup by typing **`echo $OPENAI_API_KEY`** in the terminal. It should display your API key. echo acts like print, so it prints the **`OPENAI_API_KEY` variable**
7. `**mv**` to move a file to a new directory or change its name.
    1. `mv [test.py](http://test.py) [test2.py](http://test2.py)` → change file name
    2. `mv [test.py](http://test.py) ../test` → move to a new folder called test
8. `**rm**` delete files, `rm -r [folder]` you can use this to delete a folder
9. `**which [program]**` tells you where your programm is in the folders listed in the PATH enviroment variable
10. On mac, to show enviroment variable name, you can do like `echo $HOME` this means that show the variable name HOME’s string value