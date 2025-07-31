from abc import ABC


class ReprMixin(ABC):
    """
    Класс-миксин ReprMixin, реализует вывод информации при создании экзмляра класса наследника.

    Attributes:
        *args: Неименованные атрибуты.
        **kwargs: Именованные атрибуты.
    """

    def __init__(self, *args, **kwargs):
        """
        Создаёт миксин ReprMixin.

        Attributes:
            *args: Неименованные атрибуты.
            **kwargs: Именованные атрибуты.
        """
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        all_args = ", ".join(args_repr + kwargs_repr)

        class_name = self.__class__.__name__

        print(f"{class_name}({all_args})")
