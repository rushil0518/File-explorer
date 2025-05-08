import stat

def format_permissions(mode):
    perms = ''
    perms += 'd' if stat.S_ISDIR(mode) else '-'
    perms += 'r' if mode & stat.S_IRUSR else '-'
    perms += 'w' if mode & stat.S_IWUSR else '-'
    perms += 'x' if mode & stat.S_IXUSR else '-'
    perms += 'r' if mode & stat.S_IRGRP else '-'
    perms += 'w' if mode & stat.S_IWGRP else '-'
    perms += 'x' if mode & stat.S_IXGRP else '-'
    perms += 'r' if mode & stat.S_IROTH else '-'
    perms += 'w' if mode & stat.S_IWOTH else '-'
    perms += 'x' if mode & stat.S_IXOTH else '-'
    return perms

def format_size(size):
    for unit in ['B','KB','MB','GB']:
        if size < 1024:
            return f"{size:.1f}{unit}"
        size /= 1024
    return f"{size:.1f}TB"