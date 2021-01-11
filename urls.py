from handlers import base, exception, util
from handlers.home import home
from handlers.visualize import visualize
from handlers.aesthetics import main, layoutmain

handlers = [
            # Home
            (r"/", main.MainHandler),

            # Experiment
            (r"/experiment", main.MainHandler),
            (r"/aesthetic/statement", main.StatementHandler),
            (r"/aesthetic/form", main.FormHandler),
            (r"/aesthetic/note?", main.NoteHandler),
            (r"/aesthetic/start/([0-9]+)", main.WebpageHandler),
            (r"/aesthetic/ratings", main.RatingHandler),
            (r"/aesthetic/finish", main.FinishHandler),

            # Layout Experiment
            (r"/layout/statement?", layoutmain.StatementHandler),
            (r"/layout/form", layoutmain.FormHandler),
            (r"/layout/note?", layoutmain.NoteHandler),
            (r"/layout/start/([0-9]+)", layoutmain.WebpageHandler),
            (r"/layout/ratings", layoutmain.RatingHandler),
            (r"/layout/finish", layoutmain.FinishHandler),

            # Visualization
            (r"/visualization", visualize.HomeHandler),
            (r"/visualization/sample?", visualize.MainHandler),

            # i18n
            (r"/language?", base.I18nHandler),

            # 404
            (r".*", exception.ErrorHandler),
    ]
