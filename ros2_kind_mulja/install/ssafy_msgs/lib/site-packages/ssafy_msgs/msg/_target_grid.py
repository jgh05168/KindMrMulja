# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ssafy_msgs:msg\TargetGrid.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_TargetGrid(type):
    """Metaclass of message 'TargetGrid'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('ssafy_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'ssafy_msgs.msg.TargetGrid')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__target_grid
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__target_grid
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__target_grid
            cls._TYPE_SUPPORT = module.type_support_msg__msg__target_grid
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__target_grid

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class TargetGrid(metaclass=Metaclass_TargetGrid):
    """Message class 'TargetGrid'."""

    __slots__ = [
        '_product_x',
        '_product_y',
        '_moving_zone_x',
        '_moving_zone_y',
        '_charge_x',
        '_charge_y',
    ]

    _fields_and_field_types = {
        'product_x': 'double',
        'product_y': 'double',
        'moving_zone_x': 'double',
        'moving_zone_y': 'double',
        'charge_x': 'double',
        'charge_y': 'double',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.product_x = kwargs.get('product_x', float())
        self.product_y = kwargs.get('product_y', float())
        self.moving_zone_x = kwargs.get('moving_zone_x', float())
        self.moving_zone_y = kwargs.get('moving_zone_y', float())
        self.charge_x = kwargs.get('charge_x', float())
        self.charge_y = kwargs.get('charge_y', float())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.product_x != other.product_x:
            return False
        if self.product_y != other.product_y:
            return False
        if self.moving_zone_x != other.moving_zone_x:
            return False
        if self.moving_zone_y != other.moving_zone_y:
            return False
        if self.charge_x != other.charge_x:
            return False
        if self.charge_y != other.charge_y:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def product_x(self):
        """Message field 'product_x'."""
        return self._product_x

    @product_x.setter
    def product_x(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'product_x' field must be of type 'float'"
        self._product_x = value

    @property
    def product_y(self):
        """Message field 'product_y'."""
        return self._product_y

    @product_y.setter
    def product_y(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'product_y' field must be of type 'float'"
        self._product_y = value

    @property
    def moving_zone_x(self):
        """Message field 'moving_zone_x'."""
        return self._moving_zone_x

    @moving_zone_x.setter
    def moving_zone_x(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'moving_zone_x' field must be of type 'float'"
        self._moving_zone_x = value

    @property
    def moving_zone_y(self):
        """Message field 'moving_zone_y'."""
        return self._moving_zone_y

    @moving_zone_y.setter
    def moving_zone_y(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'moving_zone_y' field must be of type 'float'"
        self._moving_zone_y = value

    @property
    def charge_x(self):
        """Message field 'charge_x'."""
        return self._charge_x

    @charge_x.setter
    def charge_x(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'charge_x' field must be of type 'float'"
        self._charge_x = value

    @property
    def charge_y(self):
        """Message field 'charge_y'."""
        return self._charge_y

    @charge_y.setter
    def charge_y(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'charge_y' field must be of type 'float'"
        self._charge_y = value
