import click


class NotRequiredIf(click.Option):
    """
    A class to handle mutually-exclusive CLI options for click.
    Created by Stephen Rauch @ https://stackoverflow.com/a/44349292/2338522
    """

    def __init__(self, *args, **kwargs):
        self.not_required_if = kwargs.pop('not_required_if')
        assert self.not_required_if, "'not_required_if' parameter required"

        kwargs_help = kwargs.get('help', '')
        kwargs['help'] = f'{kwargs_help} NOTE: This argument is mutually ' \
            f'exclusive with {self.not_required_if}'
        kwargs['help'] = kwargs['help'].strip()

        super(NotRequiredIf, self).__init__(*args, **kwargs)

    def handle_parse_result(self, ctx, opts, args):
        we_are_present = self.name in opts
        other_present = self.not_required_if in opts

        if other_present:
            if we_are_present:
                raise click.UsageError(f'Illegal usage: `{self.name}` and '
                                       f'`{self.not_required_if}` cannot be used together')
            else:
                self.prompt = None
        elif not we_are_present:
            raise click.UsageError(f'Illegal usage: One of `{self.name}` and '
                                   f'`{self.not_required_if}` is required')

        return super(NotRequiredIf, self).handle_parse_result(
            ctx, opts, args)
