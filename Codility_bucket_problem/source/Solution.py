from Codility_bucket_problem.source.Bucket import Bucket


def solution(N, Q, B, C):

    buckets = [Bucket(i) for i in range(N)]

    num_balls = len(B)
    for i in range(num_balls):
        bucket_id = B[i]
        color_id = C[i]

        color_count = add_color(buckets[bucket_id], color_id)
        if color_count == Q:
            return i + 1
    return -1


def add_color(bucket, color_id):

    matching_colors = [c for c in bucket.color_list if c.id == color_id]
    matching_color = None

    if matching_colors:
        matching_color = matching_colors[0]

    if matching_color:
        matching_color.increase_counter()
        return matching_color.counter
    else:
        new_color = bucket.add_color(color_id)
        return new_color.counter

