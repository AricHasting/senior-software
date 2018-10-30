# expects: messsage (string)
# getCommand(message) returns 
def getCommand(message):
  message = message.strip()
  split_message = message.split()
  if len(split_message) > 0:
    command = split_message[0].strip()
    if len(command) > 1 and command[0] == '/':
      return command[1:]
  return False

# expects: message (string)
# getArguments(message) returns an in-order array of the arguments provided with a command.
# This does not check if a message contains a command. Call getCommand to check first.
def getArguments(message):
  message = message.strip()
  split_message = message.split()
  if len(split_message) > 1:
    # Whitespace around args already removed by .split()
    return split_message[1:]
  return []

# expects: message (string)
# getAvatar(message) returns the first argument following a '/avatar' command.
def getAvatar(message):
  command = getCommand(message)
  if command == 'avatar':
    arguments = getArguments(message)
    if len(arguments) > 0:
      return arguments[0]
    # return '' here so that the avatar command is still validated
    return ''
  return False