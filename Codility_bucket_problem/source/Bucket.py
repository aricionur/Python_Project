from Codility_bucket_problem.source.Color import Color

class Bucket(object):

    def __init__(self, id):
        self.id = id
        self.color_list = []

    def add_color(self, color_id):
        new_color = Color(color_id)
        self.color_list.append(new_color)
        return new_color