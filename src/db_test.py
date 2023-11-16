from models import Development, Service, ServiceGroup
from app import app


with app.app_context():
    services = Service.query.all()
    for s in services:
        print(s)


with app.app_context():
    developer = Development.query.all()
    for d in developer:
        print(d)


with app.app_context():
    service_groups = ServiceGroup.query.all()
    for sg in service_groups:
        print(sg)


with app.app_context():
    services = Service.query.filter_by(service_group_id=1).all()
    service = Service.query.filter_by(service_group_id=2).all()
    for s in services:
        print(f"id=1 {s}")
    for ss in service:
        print(f"id=2 {ss}")
