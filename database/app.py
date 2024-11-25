from flask import Flask, render_template, request, redirect, url_for, flash
from db_config import get_connection

app = Flask(__name__)
app.secret_key = "secret_key"  # 用于显示消息

# 首页：显示所有图书
@app.route('/')
def index():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT book_id, book_name, book_isbn, book_author, book_publisher, interview_times, book_price FROM book")
    book = cursor.fetchall()
    conn.close()
    return render_template('index.html', books=book)

# 添加图书
@app.route('/add', methods=['GET', 'POST'])
def add_book():
    conn = get_connection()
    cursor = conn.cursor()
    if request.method == 'POST':
        # 获取表单数据并插入到数据库
        book_id = request.form['book_id']
        book_name = request.form['book_name']
        book_isbn = request.form['book_isbn']
        book_author = request.form.get('book_author', None)
        book_publisher = request.form.get('book_publisher', None)
        interview_times = request.form.get('interview_times', 0)
        book_price = request.form['book_price']
        cursor.execute("""
            INSERT INTO book (book_id, book_name, book_isbn, book_author, book_publisher, interview_times, book_price)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (book_id, book_name, book_isbn, book_author, book_publisher, interview_times, book_price))
        conn.commit()
        return redirect('/')
    conn.close()
    return render_template('add.html')


@app.route('/edit/<book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    conn = get_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        # 获取表单数据并更新数据库
        book_name = request.form['book_name']
        book_isbn = request.form['book_isbn']
        book_author = request.form.get('book_author', None)
        book_publisher = request.form.get('book_publisher', None)
        interview_times = request.form.get('interview_times', 0)
        book_price = request.form['book_price']

        # 执行更新操作
        cursor.execute("""
            UPDATE book SET
                book_name = ?, book_isbn = ?, book_author = ?, 
                book_publisher = ?, interview_times = ?, book_price = ?
            WHERE book_id = ?
        """, (book_name, book_isbn, book_author, book_publisher, interview_times, book_price, book_id))
        conn.commit()
        # 更新后重定向到书籍列表页
        return redirect('/')

    # 在GET请求时获取当前书籍数据
    cursor.execute("SELECT * FROM book WHERE book_id = ?", (book_id,))
    book = cursor.fetchone()  # 使用 fetchone() 获取单条记录
    conn.close()
    return render_template('edit.html', book=book)  # 将 book 传递到模板


# 删除图书
@app.route('/delete/<book_id>', methods=['GET', 'POST'])
def delete_book(book_id):
    conn = get_connection()
    cursor = conn.cursor()
    # 执行删除操作
    cursor.execute("DELETE FROM book WHERE book_id = ?", (book_id,))
    conn.commit()

    # 删除后重定向到首页
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
