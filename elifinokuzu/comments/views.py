from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm #CommentFormForNode, CommentFormForEdge
from dictionary.models import Node, Edge
from .models import Comment

def add_comment_to_node(request, id):
    node = get_object_or_404(Node.objects.filter(pk=id))
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.node = node
            comment.user = request.user
            comment.model_id = Node.objects.get(name=node.name).model_id
            comment.save()
            return redirect('node_detail', node.id)
    
    form = CommentForm()
    return render(request, 'comments/add_comment_to_node.html', {'form': form})

def add_comment_to_edge(request, id):
    edge = get_object_or_404(Edge.objects.filter(pk=id))
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.edge = edge
            comment.user = request.user
            # import pdb
            # pdb.set_trace()
            #comment.model_id = Edge.objects.get(name=edge.name).model_id
            comment.model_id = Edge.objects.get(source=Node.objects.get(name=edge.source.name)).model_id
            comment.save()
            return redirect('edge_detail', edge.id)
    else:
        form = CommentForm()
    return render(request, 'comments/add_comment_to_edge.html', {'form': form})
