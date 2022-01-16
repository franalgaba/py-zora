class BaseToken:
    def __repr__(self):
        from pprint import pformat

        return pformat(vars(self), indent=4, width=1)
