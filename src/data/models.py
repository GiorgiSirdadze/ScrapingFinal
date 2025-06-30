from dataclasses import dataclass

@dataclass
class Article:
    title: str
    link: str
    pub_date: str = ""
    description: str = ""
    
