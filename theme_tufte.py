import plotnine as p9


def theme_tufte(base_size=11,
                base_family='serif',
                lines=True,
                ticks=True):
    """
    Theme inspired by Chapter 6 'Data-Ink Maximization and Graphical Design` of
    Edward Tufte's 'The Visual Display of Quantitative Information`.

    Parameters
    ----------
    base_size : int, optional
        Base font size. All text sizes are scaled versions of the base font
        size. Default is 11.
    base_family : str, optional
        Base font family.
    lines : bool, optional
        Draw axis spines. Default is True.
    ticks : bool, optional
        Draw axis ticks. Default is True.

    Returns
    -------
    Plotnine theme.

    """
    ret = (
        p9.theme_bw(base_size=base_size, base_family=base_family)
        + p9.theme(
            legend_background=p9.element_blank(),
            legend_key=p9.element_blank(),
            panel_background=p9.element_blank(),
            strip_background=p9.element_blank(),
            plot_background=p9.element_rect(fill='white'),
            axis_line=p9.element_line(size=0.5),
            axis_ticks=p9.element_line(size=0.5),
            panel_grid=p9.element_blank()
        )
    )

    if not ticks:
        ret = ret + p9.theme(axis_ticks=p9.element_blank())
    if not lines:
        ret = ret + p9.theme(axis_line=p9.element_blank())

    return ret
