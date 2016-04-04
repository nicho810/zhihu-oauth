from .base import Base
from .generator import generator_of
from .other_obj import other_obj
from .simple_info import simple_info
from .streaming import streaming
from .urls import (
    ANSWER_DETAIL_URL,
    ANSWER_COLLECTIONS_URL,
    ANSWER_COMMENTS_URL,
    ANSWER_VOTERS_URL,
)

__all__ = ["Answer"]


class Answer(Base):
    def __init__(self, id, cache, session):
        super(Answer, self).__init__(id, cache, session)

    def _build_url(self):
        return ANSWER_DETAIL_URL.format(self.id)

    # ----- simple info -----

    @property
    @other_obj('people')
    def author(self):
        return None

    @property
    @streaming()
    def can_comment(self):
        return None

    @property
    @simple_info()
    def comment_count(self):
        return None

    @property
    @simple_info()
    def comment_permission(self):
        return None

    @property
    @simple_info()
    def content(self):
        return None

    @property
    @simple_info()
    def created_time(self):
        return None

    @property
    @simple_info()
    def excerpt(self):
        return None

    @property
    @simple_info()
    def id(self):
        return self._id

    @property
    @streaming('relationship')
    def if_i(self):
        return None

    @property
    @simple_info()
    def is_copyable(self):
        return None

    @property
    @simple_info()
    def is_mine(self):
        return None

    @property
    @other_obj()
    def question(self):
        return None

    @property
    @streaming()
    def suggest_edit(self):
        return None

    @property
    @simple_info()
    def thanks_count(self):
        return None

    @property
    @simple_info()
    def updated_time(self):
        return None

    @property
    @simple_info()
    def voteup_count(self):
        return None

    # ----- generators -----

    @property
    @generator_of(ANSWER_COLLECTIONS_URL)
    def collections(self):
        return None

    @property
    @generator_of(ANSWER_COMMENTS_URL)
    def comments(self):
        return None

    @property
    @generator_of(ANSWER_VOTERS_URL, 'people')
    def voters(self):
        return None