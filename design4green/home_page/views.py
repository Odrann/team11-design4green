# HOME PAGE VIEWS

from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> Test2 </h1>")

def conso(request):
    svg_buffer = StringIO()

    width, height = (500, 400)
    surface = cairo.SVGSurface(svg_buffer, width, height)

    dataSet = (
        ('dataSet 1', ((0, 1), (1, 3), (2, 2.5))),
        ('dataSet 2', ((0, 2), (1, 4), (2, 3))),
        ('dataSet 3', ((0, 5), (1, 1), (2, 0.5))),
    )

    options = {
        'legend': {'hide': True},
        'background': {'color': '#f0f0f0'},
    }

    # import pycha.bar
    # chart = pycha.bar.VerticalBarChart(surface, options)

    import pycha.line
    chart = pycha.line.LineChart(surface, options)
    chart.addDataset(dataSet)
    chart.render()

    del chart
    del surface

    response = ''
    response = HttpResponse(mimetype='image/svg+xml')
    svg_buffer.seek(0)
    response.write(svg_buffer.read())
    return response
