# Database
# 实验 10 数据库应用程序开发实验
## 二、实验内容

使用 JaveServlet/JSP/Django/Flask 或其它 Web 应用框架，构建一个web界面程序，实现以用户界面的形式对图书借阅数据库系统JY的图书表的增删改查功能。报告要求附上代码文件、设计过程以及功能测试。
## 三、实验过程

为实现一个基于Flask的Web界面程序，以用户界面的形式对图书借阅数据库系统JY的图书表的增删改查功能，我们可以按照以下步骤进行开发和设计。

### 1. **需求分析**

我们需要开发的功能包括：

* ​**查询功能**​：显示所有图书信息。
* ​**新增功能**​：添加一本新书。
* ​**编辑功能**​：修改图书信息。
* ​**删除功能**​：删除指定图书。

### 2. **设计过程**

#### **数据库设计**

数据库名为`JY`，图书表`books`结构如下：

* `book_id`
* `book_name`
* `book_isbn`
* `book_author`
* `book_publisher`
* `interview_times`
* `book_price`

#### **工具和依赖**

* ​**后端框架**​：Flask
* ​**数据库**​：SQL Server（通过`pyodbc`连接）
* ​**前端框架**​：HTML 

### 3. **代码实现**
见文件夹

### 4. **功能测试**

1. 启动应用：运行`python app.py`。
   ![image.png](/api/users/image?path=821663/images/1732548318730.png)
2. 测试功能：

* 在主页查看所有图书。
  ![3bb8e9c6881f7d9143002f66d1b48d9.png](/api/users/image?path=821663/images/1732548333014.png)
* 点击“Add New Book”添加一本图书。
  ![0ddf64cd8ecab7505afc78e591fb7ae.png](/api/users/image?path=821663/images/1732548381761.png)

![image.png](/api/users/image?path=821663/images/1732548369991.png)

* 使用“Edit”功能修改图书。
  ![339dcdeb759d71fbe78d8c26d696924.png](/api/users/image?path=821663/images/1732548417141.png)
  ![981c59ddb762197f9c925e6ce6a2daa.png](/api/users/image?path=821663/images/1732548423876.png)
* 点击“Delete”删除图书。
  ![image.png](/api/users/image?path=821663/images/1732548458747.png)

  ![3bb8e9c6881f7d9143002f66d1b48d9.png](/api/users/image?path=821663/images/1732548432883.png)
