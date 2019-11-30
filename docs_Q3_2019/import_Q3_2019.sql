--
-- Import each of the daily drive stats files for Q3 2019 ONLY
--

.mode csv
.echo on
.import ./2019/2019-07-01.csv drive_stats
.import ./2019/2019-07-02.csv drive_stats
.import ./2019/2019-07-03.csv drive_stats
.import ./2019/2019-07-04.csv drive_stats
.import ./2019/2019-07-05.csv drive_stats
.import ./2019/2019-07-06.csv drive_stats
.import ./2019/2019-07-07.csv drive_stats
.import ./2019/2019-07-08.csv drive_stats
.import ./2019/2019-07-09.csv drive_stats
.import ./2019/2019-07-10.csv drive_stats
.import ./2019/2019-07-11.csv drive_stats
.import ./2019/2019-07-12.csv drive_stats
.import ./2019/2019-07-13.csv drive_stats
.import ./2019/2019-07-14.csv drive_stats
.import ./2019/2019-07-15.csv drive_stats
.import ./2019/2019-07-16.csv drive_stats
.import ./2019/2019-07-17.csv drive_stats
.import ./2019/2019-07-18.csv drive_stats
.import ./2019/2019-07-19.csv drive_stats
.import ./2019/2019-07-20.csv drive_stats
.import ./2019/2019-07-21.csv drive_stats
.import ./2019/2019-07-22.csv drive_stats
.import ./2019/2019-07-23.csv drive_stats
.import ./2019/2019-07-24.csv drive_stats
.import ./2019/2019-07-25.csv drive_stats
.import ./2019/2019-07-26.csv drive_stats
.import ./2019/2019-07-27.csv drive_stats
.import ./2019/2019-07-28.csv drive_stats
.import ./2019/2019-07-29.csv drive_stats
.import ./2019/2019-07-30.csv drive_stats
.import ./2019/2019-07-31.csv drive_stats
.import ./2019/2019-08-01.csv drive_stats
.import ./2019/2019-08-02.csv drive_stats
.import ./2019/2019-08-03.csv drive_stats
.import ./2019/2019-08-04.csv drive_stats
.import ./2019/2019-08-05.csv drive_stats
.import ./2019/2019-08-06.csv drive_stats
.import ./2019/2019-08-07.csv drive_stats
.import ./2019/2019-08-08.csv drive_stats
.import ./2019/2019-08-09.csv drive_stats
.import ./2019/2019-08-10.csv drive_stats
.import ./2019/2019-08-11.csv drive_stats
.import ./2019/2019-08-12.csv drive_stats
.import ./2019/2019-08-13.csv drive_stats
.import ./2019/2019-08-14.csv drive_stats
.import ./2019/2019-08-15.csv drive_stats
.import ./2019/2019-08-16.csv drive_stats
.import ./2019/2019-08-17.csv drive_stats
.import ./2019/2019-08-18.csv drive_stats
.import ./2019/2019-08-19.csv drive_stats
.import ./2019/2019-08-20.csv drive_stats
.import ./2019/2019-08-21.csv drive_stats
.import ./2019/2019-08-22.csv drive_stats
.import ./2019/2019-08-23.csv drive_stats
.import ./2019/2019-08-24.csv drive_stats
.import ./2019/2019-08-25.csv drive_stats
.import ./2019/2019-08-26.csv drive_stats
.import ./2019/2019-08-27.csv drive_stats
.import ./2019/2019-08-28.csv drive_stats
.import ./2019/2019-08-29.csv drive_stats
.import ./2019/2019-08-30.csv drive_stats
.import ./2019/2019-08-31.csv drive_stats
.import ./2019/2019-09-01.csv drive_stats
.import ./2019/2019-09-02.csv drive_stats
.import ./2019/2019-09-03.csv drive_stats
.import ./2019/2019-09-04.csv drive_stats
.import ./2019/2019-09-05.csv drive_stats
.import ./2019/2019-09-06.csv drive_stats
.import ./2019/2019-09-07.csv drive_stats
.import ./2019/2019-09-08.csv drive_stats
.import ./2019/2019-09-09.csv drive_stats
.import ./2019/2019-09-10.csv drive_stats
.import ./2019/2019-09-11.csv drive_stats
.import ./2019/2019-09-12.csv drive_stats
.import ./2019/2019-09-13.csv drive_stats
.import ./2019/2019-09-14.csv drive_stats
.import ./2019/2019-09-15.csv drive_stats
.import ./2019/2019-09-16.csv drive_stats
.import ./2019/2019-09-17.csv drive_stats
.import ./2019/2019-09-18.csv drive_stats
.import ./2019/2019-09-19.csv drive_stats
.import ./2019/2019-09-20.csv drive_stats
.import ./2019/2019-09-21.csv drive_stats
.import ./2019/2019-09-22.csv drive_stats
.import ./2019/2019-09-23.csv drive_stats
.import ./2019/2019-09-24.csv drive_stats
.import ./2019/2019-09-25.csv drive_stats
.import ./2019/2019-09-26.csv drive_stats
.import ./2019/2019-09-27.csv drive_stats
.import ./2019/2019-09-28.csv drive_stats
.import ./2019/2019-09-29.csv drive_stats
.import ./2019/2019-09-30.csv drive_stats
.echo off
.mode list

--
-- The drive stats files each have a header row that labels the
-- columns.  sqlite doesn't understand this when importing from
-- CSV, so they header rows land in the table.  This removes them.
--
delete from drive_stats where model = 'model';
