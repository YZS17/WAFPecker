# WAFPecker

![image-20241221225512129](https://xu17-1326239041.cos.ap-guangzhou.myqcloud.com/xu17/202412212255908.png)

### Introduction

- `A tool for bypassing SSTI-WAF used in CTF in conjunction with fenjing.`

- SSTI vulnerability is a common problem in the Web direction of CTF, in many cases we can get the source code, so as to obtain the WAF blacklist information, this time we need to bypass according to the blacklist, and fenjing can not be used directly at all times, he needs to judge whether the payload is valid according to the response. However, the topic is often designed to have no echo, at this time we need to modify the source code, add echo, and then use fenjing tools.

- WAFPecker is a project written to solve this kind of situation. By directly entering a Blacklist, you can simulate the testable environment of fenjing, and cooperate with fenjing to generate a valid payload in the fastest way. Hope that this tool can give your some help.
- Good Luck for you! Have fun in your CTF game! 

### Usage

#### Project Structure

```/your_project_directory
/WAFPecker    
    app.py       //run this file to use this tool
    __init__.py
    views.py
    waf.py   //POST,you can also change to GET
    blacklist.txt   //write your WAF blacklist in  this file.
    requirement.txt 
```

#### Detailed Usage Steps

- `Open the blacklist.txt file, write your WAF blacklist in it like the example below.`

  ```
  ["os", "system", "eval", 'setstate', "globals", 'exec', '__builtins__', 'template', 'render', '\\','compile', 'requests', 'exit',  'pickle',"class","mro","flask","sys","base","init","config","session"]
  ```

- `Then run the app.py` 

  ![image-20241221223751030](https://xu17-1326239041.cos.ap-guangzhou.myqcloud.com/xu17/202412212237301.png)

- `Open http://127.0.0.1:5000`

  ![image-20241221224045869](https://xu17-1326239041.cos.ap-guangzhou.myqcloud.com/xu17/202412212240089.png)

  #### In conjunction with fenjing

- `Run 'fenjing webui' in your teminal.`

![image-20241221223237433](https://xu17-1326239041.cos.ap-guangzhou.myqcloud.com/xu17/202412212232566.png)

- `At last , We can optain the payload that can bypass the WAF.`

```
{%set iq='so'[::-1]%}{{cycler.next['__g''lobals__']['_''_builtins__'].__import__(iq).popen('ls').read()}}
```

