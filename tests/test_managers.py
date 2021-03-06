#    Copyright (C) 2020 Presidenza del Consiglio dei Ministri.
#    Please refer to the AUTHORS file for more information.
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <https://www.gnu.org/licenses/>.

from unittest.mock import PropertyMock, patch

from pytest import raises

from immuni_common.core.exceptions import ImmuniException
from immuni_exposure_ingestion.core.managers import Managers, managers


def test_exposure_mongo_failure() -> None:
    with patch.object(Managers, "_exposure_mongo", new_callable=PropertyMock) as mock:
        mock.return_value = None
        with raises(ImmuniException):
            managers.exposure_mongo


def test_analytics_redis_failure() -> None:
    with patch.object(Managers, "_analytics_redis", new_callable=PropertyMock) as mock:
        mock.return_value = None
        with raises(ImmuniException):
            managers.analytics_redis


def test_otp_redis_failure() -> None:
    with patch.object(Managers, "_otp_redis", new_callable=PropertyMock) as mock:
        mock.return_value = None
        with raises(ImmuniException):
            managers.otp_redis


def test_celery_redis_failure() -> None:
    with patch.object(Managers, "_celery_redis", new_callable=PropertyMock) as mock:
        mock.return_value = None
        with raises(ImmuniException):
            managers.celery_redis
