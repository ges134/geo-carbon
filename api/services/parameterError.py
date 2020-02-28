class ParameterError(Exception):
  def __init__(self, field: str, message: str):
    self.field = field
    self.message = message

  def getDetailedMessage(self) -> str:
    return 'Error in request field: ' + self.field + '. ' + self.message