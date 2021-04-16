# Active Directory


class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    response = False

    for group_user in group.get_users():
        if group_user == user:
            return True

    for subgroup in group.get_groups():
        response |= is_user_in_group(user, subgroup)

    return response


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)

child_user = "child_user"
child.add_user(child_user)
parent.add_group(child)

no_parent_user = "no_parent_user"
no_parent_group = Group("no_parent_child")
no_parent_group.add_user(no_parent_user)

assert is_user_in_group(sub_child_user, parent) == True
assert is_user_in_group(child_user, parent) == True
assert is_user_in_group(sub_child_user, child) == True
assert is_user_in_group(child_user, sub_child) == False
assert is_user_in_group(None, sub_child) == False
assert is_user_in_group("no_parent_user", no_parent_group) == True