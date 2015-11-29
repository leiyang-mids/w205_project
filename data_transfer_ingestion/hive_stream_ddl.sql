-- stream table

drop table m_stream;
create table m_stream as
  select
    seg.id as seg_id,
    cast(str.distance as double) as distance,
    cast(str.altitude as double) as altitude,
    cast(str.latitude as double) as latitude,
    cast(str.longitude as double) as longitude
  from e_streams str
  inner join m_segment seg on str.seg_id = seg.id;
