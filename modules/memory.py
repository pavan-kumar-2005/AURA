conversation=[]
def add_memory(role,message):
    conversation.append({
        "role":role,
        "content":message
    })
def get_memory():
    return conversation