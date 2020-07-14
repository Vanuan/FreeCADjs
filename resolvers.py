import FreeCAD
from schema import Setting, Settings, SettingGroup

def get_dump():
    dump = FreeCAD.ConfigDump()
    dump_array = [Setting(name=k, value=v) for (k, v) in dump.items()]
    return dump_array

def get_version():
    major = FreeCAD.ConfigGet("BuildVersionMajor")
    minor = FreeCAD.ConfigGet("BuildVersionMinor")
    return f'{major}.{minor}'

def get_group_settings(group):
    contents = group.GetContents()
    if contents:
      #return [Setting(name=name, value=value, fc_type=fc_type) for (fc_type, name, value) in filter(None, contents)]
      return [(name, value) for (fc_type, name, value) in filter(None, contents)]
    return []

def get_group(group_name, parent_group):
    group = parent_group.GetGroup(group_name)
    print(group_name)
    print(group)
    print(get_group_settings(group) + get_groups(group))

    return (group_name, dict(get_group_settings(group) + get_groups(group))) #SettingGroup(name=group_name, settings=get_group_settings(group))

def get_groups(group):
    group_names = group.GetGroups()
    groups = [get_group(group_name, group) for group_name in group_names]
    return groups

def get_user():
    root = dict((
        ('BaseApp', dict(get_groups(FreeCAD.ParamGet('User parameter:BaseApp')))),
        ('Tux', dict(get_groups(FreeCAD.ParamGet('User parameter:Tux'))))
    ))
    return root

def get_system():
    root = dict((
        ('Modules', dict(get_groups(FreeCAD.ParamGet('System parameter:Modules')))),
        ('AdditionalModulePaths', dict(get_groups(FreeCAD.ParamGet('System parameter:AdditionalModulePaths')))),
        ('Test', dict(get_groups(FreeCAD.ParamGet('System parameter:Test'))))
    ))
    return root

def get_settings():
    return Settings(version = get_version(), dump = get_dump(), user = get_user(), system = get_system())
