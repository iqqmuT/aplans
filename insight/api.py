from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from django_orghierarchy.models import Organization, OrganizationClass

from actions.models import Action, Plan
from aplans.utils import register_view_helper
from .generator import ActionGraphGenerator, OrganizationGraphGenerator

all_views = []


def register_view(klass, *args, **kwargs):
    return register_view_helper(all_views, klass, *args, **kwargs)


class InsightViewSet(viewsets.ViewSet):
    def list(self, request):
        params = request.query_params
        object_type = params.get('type', 'action').strip().lower()
        if object_type == 'organization':
            orgs = Organization.objects.filter(dissolution_date__isnull=True)
            classes = OrganizationClass.objects.all()
            generator = OrganizationGraphGenerator(request=request, orgs=orgs, classifications=classes)
        else:
            plan_id = params.get('plan', '').strip()
            if not plan_id:
                raise ValidationError("You must supply a 'plan' filter")
            try:
                plan = Plan.objects.get(identifier=plan_id)
            except Plan.DoesNotExist:
                raise ValidationError("Plan %s does not exist" % plan_id)

            action_id = params.get('action', '').strip()
            if action_id:
                try:
                    action = Action.objects.get(id=action_id, plan=plan)
                except Action.DoesNotExist:
                    raise ValidationError("Action %s does not exist in plan %s" % (action_id, plan_id))
            else:
                action = None

            if action is not None:
                generator = ActionGraphGenerator(request=request, plan=plan, traverse_forward_only=True)
                generator.add_node(action)
            else:
                generator = ActionGraphGenerator(request=request, plan=plan, traverse_forward_only=False)
                actions = Action.objects.filter(plan=plan, indicators__isnull=False)
                for act in actions:
                    generator.add_node(act)

        graph = generator.get_graph()
        return Response(graph)


register_view(klass=InsightViewSet, name='insight', basename='insight')
