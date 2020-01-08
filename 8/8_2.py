from common import diff

print(diff(lambda line: line.replace("\\", "\\\\")
                            .replace("\"", "\\\"") + "__"))
