# Logger

Module to facilitate the creation of logs with logging

### **Installation**

```powershell
pip install Logger
```

### **Example**: 

Types of log

```python
DEBUG = 0
INFO = 1
WARNING = 2
ERROR = 3
CRITICAL = 4
```

```python
 from Logger import log
 
 #log.create("filename", "text", type_logger)
 log.create("skynet_log", "deu merda ......", log.ERROR)
 ```
