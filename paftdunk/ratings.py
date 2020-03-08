def serendipity(alpha=1, beta=1):
    def rating(d):
        good_stuff = (d["n_overlap"] / d["n_uniq_from"]) ** alpha
        bad_stuff = (d["n_uniq_to"] / d["n_total_user"]) ** beta
        return good_stuff / bad_stuff

    return rating
