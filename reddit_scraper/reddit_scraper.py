from flask import Flask, render_template, jsonify
from Forms import UserNameForm
from scraper import *
from user import Comment
from user.SubredditList import SubredditList

app = Flask(__name__)
app.config.from_object('config')


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def hello_world():
    name = None
    form = UserNameForm()
    if form.validate_on_submit():
        user = form.user.data
        comment_list = scrape_user(user, 100, "")
        total = sum(get_comment_count(comment_list).values())
        sub_list = make_subreddit_list(comment_list)
        sub_list.apply_total_comments(total)
        sub_list.total_ups_and_downs()
        return render_template("user.html", form=form, user=user, total=total, comment_list=comment_list, sub_list=sub_list)

    return render_template("index.html", form=form)


if __name__ == '__main__':
    app.debug=True
    app.run()
