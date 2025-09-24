from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from auth.domain.operating_hours import OperatingHours
from auth.domain.branches import Branches
from auth.domain.postmats import Postmats
from auth.domain.senders import Senders
from auth.domain.receivers import Receivers
from auth.domain.delivery_address import DeliveryAddress
from auth.domain.packages import Packages
from auth.domain.package_tracking import PackageTracking
from auth.domain.branches_senders import BranchesSenders
from auth.domain.couriers import Couriers
from auth.domain.courier_branches import CourierBranches
from auth.domain.payment import Payment