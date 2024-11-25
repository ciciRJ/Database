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
   ![b957298c51e5178c0d4c9d39c89d35b](https://github.com/user-attachments/assets/67e979a7-d23a-49be-822a-b45e82df2b75)

2. 测试功能：

* 在主页查看所有图书。
  ![3bb8e9c6881f7d9143002f66d1b48d9](https://github.com/user-attachments/assets/dde6abdd-7055-4c53-8f8d-7e1cca2ef468)

* 点击“Add New Book”添加一本图书。
  ![a3b4ba6c39c64eb01879af75c43a1c1](https://github.com/user-attachments/assets/3d949e25-7517-4401-9307-738dbd6f64d0)

  ![7b3c807aaad80b7e67188c7e0ab09d8](https://github.com/user-attachments/assets/397c783e-c839-4924-87dc-d897a8074daa)


* 使用“Edit”功能修改图书。
  ![befd19dc0ef7fc2a5e83fbaef54df2d](https://github.com/user-attachments/assets/9db7f3f4-aeea-4e36-a885-255e31364052)

  ![981c59ddb762197f9c925e6ce6a2daa](https://github.com/user-attachments/assets/998cd8d5-9474-4dc7-8028-04dbf421a898)

* 点击“Delete”删除图书。
  ![3bb8e9c6881f7d9143002f66d1b48d9](https://github.com/user-attachments/assets/9a71b34a-c2db-4b5d-a84e-57b18dfed5b1)

