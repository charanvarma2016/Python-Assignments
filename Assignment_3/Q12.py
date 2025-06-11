# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 17:12:33 2025

@author: saikr
"""
"""12. Simple Social Media Post System
Create classes for User, Post, and Comment. Implement functionality to like, comment,
and share posts, and display a timeline of user activities."""

import datetime

# Comment class
class Comment:
    def __init__(self, user, content):
        self.user = user
        self.content = content
        self.timestamp = datetime.datetime.now()

    def display(self):
        return f"{self.user.name} commented: '{self.content}' at {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"


# Post class
class Post:
    def __init__(self, user, content):
        self.user = user
        self.content = content
        self.timestamp = datetime.datetime.now()
        self.likes = 0
        self.comments = []
        self.shares = 0

    def like(self):
        self.likes += 1

    def comment(self, user, content):
        new_comment = Comment(user, content)
        self.comments.append(new_comment)

    def share(self):
        self.shares += 1

    def display(self):
        print(f"{self.user.name} posted at {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}:")
        print(f"  {self.content}")
        print(f"  Likes: {self.likes}, Shares: {self.shares}")
        print(f"  Comments:")
        if self.comments:
            for c in self.comments:
                print(f"    - {c.display()}")
        else:
            print("    No comments yet.")
        print("-" * 50)


# User class
class User:
    def __init__(self, name):
        self.name = name
        self.timeline = []

    def create_post(self, content):
        post = Post(self, content)
        self.timeline.append(post)
        return post

    def view_timeline(self):
        print(f"\n{self.name}'s Timeline:")
        if not self.timeline:
            print("  No posts yet.")
        for post in self.timeline:
            post.display()


# Example 
if __name__ == "__main__":
    # Create users
    alice = User("Alice")
    bob = User("Bob")

    # Alice creates a post
    post1 = alice.create_post("Hello, world!")

    # Bob likes, shares and comments on Alice's post
    post1.like()
    post1.like()
    post1.share()
    post1.comment(bob, "Nice post, Alice!")

    # Alice creates another post
    post2 = alice.create_post("Having a great day!")

    # Bob comments on second post
    post2.comment(bob, "That's great to hear!")

    # View timelines
    alice.view_timeline()
