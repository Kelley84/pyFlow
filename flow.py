#flow util

def newFlowObj(long, short, bal):
    obj = FlowObj(nameLong=long, nameShort=short, balance=bal)
    obj.save()
    
def showFlowObj():
    from flow.models import FlowObj
    print(FlowObj.objects.all())