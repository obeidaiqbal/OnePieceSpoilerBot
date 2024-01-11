from email.message import EmailMessage
import ssl
import smtplib
import praw

email_sender = ' '
email_password = ' '
subreddit_search = 'Spoilers'
   
reddit = praw.Reddit(
    client_id = " ",
    client_secret = " ",
    user_agent = "OnePieceSpoilerChecker by u/chikachika-boomboom",
)

subreddit = reddit.subreddit("OnePiece")
hot_posts = subreddit.hot(limit = 1)

for post in hot_posts:
    if (subreddit_search in post.title) == False:
        print('No Spoiler Yet')
        exit()
    subject = "One Piece Spoilers Are Out!"
    body = f"The reddit post {post.title} made by u/{post.author} confirms that spoilers are out for One Piece. Be careful browsing socials to aviod spoilers!\n\n\nLink to Post: {post.url}"

    file = open('emails.txt', 'r')
    while True:
        email_receiver = file.readline()
        if not email_receiver:
            break
        em = EmailMessage()
        em['From'] = email_sender
        em['Subject'] = subject
        em.set_content(body)
        em['To'] = email_receiver
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
