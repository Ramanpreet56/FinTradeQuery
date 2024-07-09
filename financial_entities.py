from dataclasses import dataclass

@dataclass
class Text:
    content: str
    
    def replace_placeholders(self, replacements):
        for placeholder, replacement in replacements.items():
            self.content = self.content.replace(placeholder, str(replacement))
        return self.content
    
        
@dataclass
class Table:
    data: list

@dataclass
class Report:
    trades: list
    name: str
    account_id: int
    phone: int
    entity: str
    