class Config:
    
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    pass

class ProductionConfig(Config):
    pass


config = {
    "production" : ProductionConfig,
    "development" : DevelopmentConfig,
    
    "default" : DevelopmentConfig
}