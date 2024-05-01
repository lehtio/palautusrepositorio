from unittest.mock import Mock

mock = Mock()

print(mock)

mock.foo.bar.return_value = "Foobar"

print(mock.foo.bar())

mock.foo.bar.side_effect = lambda name: f"{name}: Foobar"

print(mock.foo.bar("Kalle"))

get_name_mock = Mock(return_value="Matti")

print(get_name_mock())

mock.foo.bar.assert_called()

mock.foo.doo.assert_not_called()

exit()
