from graphene import ObjectType, InputObjectType, String, ID, Int, Field, List
from graphene.types.json import JSONString
from graphene.types.generic import GenericScalar

# Pacakges
class Package(ObjectType):
    archive = Int(required=True)
    backlog = Int(required=True)
    color = String(required=True)
    commits = Field(lambda: Commit)
    contributors = Field(lambda: Contributors)
    created_at = String()
    created_by = ID()
    description = String(required=True)
    forks = Int()
    id = ID(required=True)
    issues = Int(required=True)
    language = String(required=True)
    last_commit = Field(lambda: LastCommit)
    last_release = Field(lambda: LastRelease)
    license = String()
    mentionable_users = Int(required=True)
    owner_avatar = String(required=True)
    owner_name = String(required=True)
    package_name = String(required=True)
    package_avatar = String()
    production = Int(required=True)
    pull_requests = Int(required=True)
    readme = Field(lambda: Readme)
    releases = Int()
    repo_url = String(required=True)
    stars = Int(required=True)
    tags = List(String)
    trial = Int(required=True)
    updated_at = String()
    watchers = Int()
    website_url = String()


class PackageSummary(ObjectType):
    color = String(required=True)
    description = String(required=True)
    issues = Int(required=True)
    language = String(required=True)
    owner_avatar = String(required=True)
    owner_name = String(required=True)
    package_name = String(required=True)
    stars = Int(required=True)


class PackageInput(InputObjectType):
    owner_name = String(required=True)
    package_name = String(required=True)


class PackageFilter(InputObjectType):
    language = String()


class Readme(ObjectType):
    extension = String()
    text = String()

    def resolve_extension(root, args, context, info):
        return root['extension']

    def resolve_text(root, args, context, info):
        return root['text']


class LastRelease(ObjectType):
    description = String()
    name = String(required=True)
    published_at = String(required=True)
    url = String(required=True)

    def resolve_description(root, args, context, info):
        return root['description']

    def resolve_name(root, args, context, info):
        return root['name']

    def resolve_published_at(root, args, context, info):
        return root['published_at']

    def resolve_url(root, args, context, info):
        return root['url']


class LastCommit(ObjectType):
    author = Field(lambda: Author)
    commit_url = String(required=True)
    message = String(required=True)
    oid = ID(required=True)

    def resolve_author(root, args, context, info):
        return root['author'] if 'author' in root else {}

    def resolve_commit_url(root, args, context, info):
        return root['commit_url'] if 'commit_url' in root else ''

    def resolve_message(root, args, context, info):
        return root['message'] if 'message' in root else ''

    def resolve_oid(root, args, context, info):
        return root['oid'] if 'oid' in root else ''


class Commit(ObjectType):
    total = Int(required=True)
    url = String(required=True)

    def resolve_total(root, args, context, info):
        return root['total']

    def resolve_url(root, args, context, info):
        return root['url']


class Contributors(ObjectType):
    top_100 = List(lambda: Contributor)
    total = Int()

    def resolve_top_100(root, args, context, info):
        return root['top_100']

    def resolve_total(root, args, context, info):
        return root['total']


class Contributor(ObjectType):
    avatar = String()
    url = String()
    username = String()

    def resolve_avatar(root, args, context, info):
        return root['author']['avatar']

    def resolve_url(root, args, context, info):
        return root['author']['url']

    def resolve_username(root, args, context, info):
        return root['author']['username']


class Author(ObjectType):
    date = String()
    name = String()
    email = String()

    def resolve_date(root, args, context, info):
        return root['date'] if 'date' in root else ''

    def resolve_name(root, args, context, info):
        return root['name'] if 'name' in root else ''

    def resolve_email(root, args, context, info):
        return root['email'] if 'email' in root else ''


# Users
class User(ObjectType):
    id = ID(required=True)
    avatar = String(required=True)
    bio = String()
    company = String()
    connections = List(lambda: UserConnection)
    created_at = String(required=True)
    email = String(required=True)
    kanban_boards = List(String)
    kanban_cards = List(lambda: KanbanCard)
    name = String(required=True)
    total_subscriptions = Int(required=True)
    total_packages = Int(required=True)
    updated_at = String()
    username = String(required=True)
    website = String()


class UserConnection(ObjectType):
    avatar = String()
    bio = String()
    name = String()
    username = String(required=True)


class UserConnectionInput(InputObjectType):
    username = String(required=True)


class KanbanCard(ObjectType):
    board = String(required=True)
    owner_name = String(required=True)
    package_name = String(required=True)

    def resolve_board(root, args, context, info):
        return root['board']

    def resolve_owner_name(root, args, context, info):
        return root['owner_name']

    def resolve_package_name(root, args, context, info):
        return root['package_name']


class KanbanCardInput(InputObjectType):
    board = String(required=True)
    owner_name = String(required=True)
    package_name = String(required=True)


class CurrentUserInput(InputObjectType):
    username = String(required=True)
    token = String(required=True)


class UserInput(InputObjectType):
    username = String(required=True)


class UserKanbanPackage(ObjectType):
    color = String()
    description = String()
    issues = String()
    language = String()
    owner_avatar = String()
    owner_name = String(required=True)
    package_id = ID(required=True)
    package_name = String(required=True)
    stars = String()
    status = String(required=True)
    user_id = ID()
    username = String(required=True)


class UserKanbanPackageInput(InputObjectType):
    username = String(required=True)
