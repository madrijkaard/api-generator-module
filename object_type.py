from enum import Enum

ObjectType = Enum('ObjectType', (
    'byte',
    'short',
    'int',
    'long',
    'float',
    'double',
    'char',
    'boolean',
    'Object',
    'String',
    'Integer', 
    'Long', 
    'Double', 
    'Float', 
    'Character', 
    'Boolean',
    'java.math.BigDecimal',
    'java.util.ArrayList',
    'java.util.LinkedList',
    'java.util.HashSet',
    'java.util.TreeSet',
    'java.util.HashMap',
    'java.util.LinkedHashMap',
    'java.util.LinkedHashSet',
    'java.util.PriorityQueue',
    'java.util.Stack',
    'java.util.Queue',
    'java.util.Deque',
    'java.util.List',
    'java.util.Map',
    'java.util.Set',
    'java.time.LocalDate',
    'java.time.LocalTime',
    'java.time.LocalDateTime',
    'java.time.ZonedDateTime',
    'java.time.Instant',
    'java.time.Duration',
    'java.time.Period',
    'java.time.format.DateTimeFormatter',
    'java.time.format.DateTimeParseException',
    'java.time.temporal.TemporalAdjusters',
    'java.time.zone.ZoneId',
    'java.time.zone.ZoneOffsetTransition',
    'java.time.zone.ZoneRules'
))
