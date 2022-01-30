from django.db import models


class Bloger(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=1000, blank=True, null=True)
    user = models.ForeignKey(Bloger, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{} by {}'.format(self.title, self.user)


class CommentPost(models.Model):
    user_comment = models.ForeignKey(Bloger, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(max_length=150, null=True, blank=True)
    comment_to_comment = models.ForeignKey('Blog.CommentPost', null=True, blank=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return '{} commented {}'.format(self.user_comment, self.post)


class LikeComment(models.Model):
    user_name = models.ForeignKey(Bloger, on_delete=models.CASCADE)
    like_comment = models.ForeignKey(CommentPost, on_delete=models.CASCADE)

    def __str__(self):
        return '{} liked comment {}'.format(self.user_name, self.like_comment)


class DisslikeComment(models.Model):
    user_name = models.ForeignKey(Bloger, on_delete=models.CASCADE)
    disslikecomment = models.ForeignKey(CommentPost, on_delete=models.CASCADE)

    def __str__(self):
        return '{} dissliked comment {}'.format(self.user_name, self.disslikecomment)


class LikePost(models.Model):
    user_name = models.ForeignKey(Bloger, on_delete=models.CASCADE)
    like_post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return '{} liked post {}'.format(self.user_name, self.like_post)


class DisslikePost(models.Model):
    user_name = models.ForeignKey(Bloger, on_delete=models.CASCADE)
    disslike_post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return '{} dissliked post {}'.format(self.user_name, self.disslike_post)
