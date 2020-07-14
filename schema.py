from graphene import String, ObjectType, List, Field, JSONString

class Setting(ObjectType):
    name = String()
    value = String()
    fc_type = String()

class SettingGroup(ObjectType):
    name = String()
    settings = List(Setting)
    groups = List(lambda: SettingGroup)

class Settings(ObjectType):
    version = String()
    dump = List(Setting)
    user = Field(JSONString)
    system = Field(JSONString)
